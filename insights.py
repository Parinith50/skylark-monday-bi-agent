"use client";

import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch(
        "https://skylark-monday-bi-agent-7xi7.onrender.com/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question,
          }),
        }
      );

      const data = await response.json();

      setAnswer(data.answer);
    } catch (err) {
      setAnswer("Unable to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-slate-100 flex justify-center items-center p-10">
      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-3xl">

        <h1 className="text-4xl font-bold text-center">
          Skylark BI Agent
        </h1>

        <p className="text-center text-gray-500 mt-2">
          Ask questions about your Monday.com business data
        </p>

        <textarea
          className="w-full border rounded-xl p-4 mt-8 h-32"
          placeholder="Example: How is our pipeline?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          onClick={askQuestion}
          disabled={loading}
          className="w-full mt-5 bg-blue-600 text-white rounded-xl py-3 hover:bg-blue-700 transition"
        >
          {loading ? "Analyzing..." : "Ask BI Agent"}
        </button>

        {answer && (
          <div className="mt-8 bg-gray-100 rounded-xl p-6 whitespace-pre-wrap">
            <h2 className="text-xl font-semibold mb-3">
              Response
            </h2>

            {answer}
          </div>
        )}
      </div>
    </main>
  );
}