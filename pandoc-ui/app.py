import os, shutil, subprocess, tempfile, uuid, zipfile
from flask import Flask, request, send_file, jsonify, Response

def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

    @app.get("/")
    def root():
        return Response(open("index.html","rb").read(), mimetype="text/html")

    @app.post("/api/convert")
    def convert():
        to_fmt = (request.form.get("to") or "").strip().lower()
        frm = (request.form.get("from") or "").strip().lower()
        title = (request.form.get("title") or "").strip()
        author = (request.form.get("author") or "").strip()
        toc = request.form.get("toc") == "on"
        number_sections = request.form.get("number_sections") == "on"
        citeproc = request.form.get("citeproc") == "on"
        extra_args = (request.form.get("extra_args") or "").strip()

        if not to_fmt:
            return jsonify(error="Missing 'to' format"), 400

        f = request.files.get("file")
        text = request.form.get("text", "")

        if not f and not text:
            return jsonify(error="Provide either a file or text"), 400

        work = tempfile.mkdtemp(prefix="pandocui_")
        try:
            # sorgente
            if f:
                origname = f.filename or "input"
                in_path = os.path.join(work, origname)
                f.save(in_path)
            else:
                in_path = os.path.join(work, "input.md")
                with open(in_path, "w", encoding="utf-8") as fh:
                    fh.write(text)

            # opzionale: resources.zip -> estrai e usa come resource-path
            res_zip = request.files.get("resources")
            if res_zip and res_zip.filename:
                zpath = os.path.join(work, "resources.zip")
                res_zip.save(zpath)
                with zipfile.ZipFile(zpath) as zf:
                    zf.extractall(work)

            out_basename = f"{uuid.uuid4().hex}.{to_fmt}"
            out_path = os.path.join(work, out_basename)

            cmd = ["pandoc", in_path, "-o", out_path]

            # from esplicito (altrimenti auto)
            if frm:
                cmd.extend(["-f", frm])

            # metadati & opzioni comuni
            if title:
                cmd.extend(["--metadata", f"title={title}"])
            if author:
                cmd.extend(["--metadata", f"author={author}"])
            if toc:
                cmd.append("--toc")
            if number_sections:
                cmd.append("--number-sections")
            if citeproc:
                cmd.append("--citeproc")

            # template opzionale
            tpl = request.files.get("template")
            if tpl and tpl.filename:
                tpl_path = os.path.join(work, "template")
                tpl.save(tpl_path)
                cmd.extend(["--template", tpl_path])

            # CSL opzionale (stile bibliografico)
            csl = request.files.get("csl")
            if csl and csl.filename:
                csl_path = os.path.join(work, "style.csl")
                csl.save(csl_path)
                cmd.extend(["--csl", csl_path])

            # Reference docx/odt opzionale
            refdoc = request.files.get("reference_doc")
            if refdoc and refdoc.filename:
                ref_path = os.path.join(work, refdoc.filename)
                refdoc.save(ref_path)
                cmd.extend(["--reference-doc", ref_path])

            # Se abbiamo estratto risorse, abilita resource-path
            if res_zip and res_zip.filename:
                cmd.extend(["--resource-path=.:"])

            # Argomenti avanzati liberi
            if extra_args:
                cmd.extend(extra_args.split())

            # PDF via LaTeX: se non specificato un engine, usa XeLaTeX
            if to_fmt == "pdf" and not any(a.startswith("--pdf-engine") for a in cmd):
                cmd.extend(["--pdf-engine=xelatex"])

            run = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode != 0 or not os.path.exists(out_path):
                return jsonify(error="Pandoc failed", log=run.stdout, cmd=cmd), 500

            download = (request.form.get("outname") or f"output.{to_fmt}").strip() or f"output.{to_fmt}"
            download = download.replace("/", "_").replace("\\", "_")

            return send_file(out_path, as_attachment=True, download_name=download)

        finally:
            shutil.rmtree(work, ignore_errors=True)

    @app.get("/api/health")
    def health():
        return jsonify(status="ok")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))