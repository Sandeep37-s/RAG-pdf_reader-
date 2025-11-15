from flask import Flask, render_template, request
from pdf_qa import create_pdf_vectorstore, get_pdf_answer
import os

app = Flask(__name__)

VECTORSTORE_CACHE = None

@app.route("/", methods=["GET", "POST"])
def index():
    global VECTORSTORE_CACHE

    if request.method == "POST":
        pdf = request.files.get("pdf")
        question = request.form.get("question")
        answer = None
        error = None

        try:
            if pdf:
                pdf_path = "uploaded.pdf"
                pdf.save(pdf_path)
                VECTORSTORE_CACHE = create_pdf_vectorstore(pdf_path)
                print("✅ PDF uploaded and vectorstore created")

            if VECTORSTORE_CACHE and question:
                print("🧠 Sending question to OpenRouter:", question)
                answer = get_pdf_answer(VECTORSTORE_CACHE, question)
                print("✅ Answer received:", answer)

                # Redirect to result.html with answer and question
                return render_template("result.html", question=question, answer=answer)

        except Exception as e:
            import traceback
            error = str(e)
            print("\n❌ ERROR OCCURRED:\n", traceback.format_exc())
            return render_template("result.html", question=question, answer=None, error=error)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
