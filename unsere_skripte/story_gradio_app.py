#%% Pakete
from pathlib import Path
import os

import gradio as gr
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter

# .env im Projekt-Root laden (unabhängig vom Arbeitsverzeichnis)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# %% Promptvorlage
# Aufgabe: Geschichte über eine Person ({character}) in einer Situation ({location})
messages = [
    (
        "system",
        """
        Du schreibst kurze, anschauliche Geschichten auf Deutsch.
        Die Geschichte handelt von der genannten Person an dem genannten Ort.
    """,
    ),
    (
        "user",
        "Schreibe eine Geschichte über {character} in folgender Situation: {location}.",
    ),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# %% Modell
MODEL_NAME = "deepseek/deepseek-v4.1-flash"
model = ChatOpenRouter(model=MODEL_NAME, temperature=1)

# %% Kette: Prompt Template | LLM
chain = prompt_template | model


# %% Callback für die Gradio-App (streamt die Antwort)
def schreibe_geschichte(character: str, location: str):
    character = (character or "").strip()
    location = (location or "").strip()

    if not character or not location:
        yield "⚠️ Bitte gib sowohl eine Person als auch eine Situation/einen Ort an."
        return

    if not os.getenv("OPENROUTER_API_KEY"):
        yield "❌ `OPENROUTER_API_KEY` fehlt. Bitte in der `.env` im Projekt-Root hinterlegen."
        return

    text = ""
    try:
        for chunk in chain.stream({"character": character, "location": location}):
            if chunk.content:
                text += chunk.content
                yield text
    except Exception as e:  # noqa: BLE001 - Fehler direkt in der UI anzeigen
        yield f"❌ Fehler bei der Anfrage: {e}"


# %% Gradio-Oberfläche
with gr.Blocks(title="Geschichten-Generator") as demo:
    gr.Markdown(
        """
        # 📖 Geschichten-Generator
        Wähle **links eine Person** und **rechts eine Situation** – beide Felder sind
        frei eingebbar und beliebig miteinander kombinierbar. Die Beispiel-Listen
        füllen jeweils nur ihr eigenes Feld.
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🧑 Person")
            character_in = gr.Textbox(
                label="Person",
                placeholder="z. B. Harry Potter",
                show_label=False,
            )
            gr.Examples(
                examples=[
                    "Harry Potter",
                    "Ada Lovelace",
                    "Ein kleiner Oktopus",
                    "Sherlock Holmes",
                    "Ein müder Programmierer",
                    "Marie Curie",
                ],
                inputs=character_in,
                label="Personen – Klick füllt nur dieses Feld",
            )

        with gr.Column(scale=1):
            gr.Markdown("### 🌍 Situation / Ort")
            location_in = gr.Textbox(
                label="Situation / Ort",
                placeholder="z. B. auf der International Space Station",
                show_label=False,
            )
            gr.Examples(
                examples=[
                    "International Space Station",
                    "einem Flohmarkt in Berlin",
                    "einer überfüllten U-Bahn",
                    "einem Burger-Restaurant im Jahr 2026",
                    "einem Montagmorgen ohne Kaffee",
                    "einem Strandurlaub auf Island",
                ],
                inputs=location_in,
                label="Situationen – Klick füllt nur dieses Feld",
            )

    generate_btn = gr.Button("Geschichte schreiben ✨", variant="primary")
    story_out = gr.Markdown(label="Geschichte", value="_Noch keine Geschichte erzeugt._")

    generate_btn.click(
        fn=schreibe_geschichte,
        inputs=[character_in, location_in],
        outputs=story_out,
    )
    character_in.submit(
        fn=schreibe_geschichte,
        inputs=[character_in, location_in],
        outputs=story_out,
    )
    location_in.submit(
        fn=schreibe_geschichte,
        inputs=[character_in, location_in],
        outputs=story_out,
    )


# %%
if __name__ == "__main__":
    demo.queue().launch()
