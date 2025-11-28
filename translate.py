import asyncio

from docutranslate.exporter.docx.docx2html_exporter import Docx2HTMLExporterConfig
from docutranslate.translator.ai_translator.docx_translator import DocxTranslatorConfig
from docutranslate.workflow.docx_workflow import DocxWorkflowConfig, DocxWorkflow
import json
from pathlib import Path


async def main():
    # Load glossary dictionary from a local JSON file (required)
    glossary_path = Path("glossary.json")
    if not glossary_path.exists():
        print("Glossary file not found: glossary.json")
        exit(1)
    try:
        glossary_dict = json.loads(glossary_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Failed to parse glossary file: {e}")
        exit(1)
    # 1. Build translator configuration
    translator_config = DocxTranslatorConfig(
        base_url="https://api.openai.com/v1/",
        api_key="",                                   # ITT ADD MEG AZ API KULCSOD
        model_id="gpt-5.1",
        to_lang="English",
        thinking="default",  # Use "default" to let the system automatically handle reasoning_effort
        insert_mode="replace",  # Options: "replace", "append", "prepend"
        separator="\n",  # Separator used in "append" and "prepend" modes
        glossary_dict=glossary_dict,  # Provide a glossary to align terminology
        glossary_generate_enable=True,  # Uncomment to auto-generate glossary during translation
    )

    # 2. Build main workflow configuration
    workflow_config = DocxWorkflowConfig(
        translator_config=translator_config,
        html_exporter_config=Docx2HTMLExporterConfig(cdn=True)
    )

    # 3. Instantiate the workflow
    workflow = DocxWorkflow(config=workflow_config)

    # 4. Read the file and execute translation
    #
    #  ITT ADD MEG A FORRÁSFÁJL NEVÉT
    #
    workflow.read_path("uzinfo_mini.docx")
    await workflow.translate_async()
    # Or use the synchronous method
    # workflow.translate()

    # 5. Save the result
    #
    #  ITT ADD MEG A CÉLFÁJL NEVÉT
    #
    workflow.save_as_docx(name="translated_uzinfo_mini.docx")
    print("DOCX file saved.")

    # You can also export the translated DOCX as bytes
    text_bytes = workflow.export_to_docx()


if __name__ == "__main__":
    asyncio.run(main())