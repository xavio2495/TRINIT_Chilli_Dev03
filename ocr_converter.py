import subprocess
import uuid
import requests
import re
import gradio as gr
from nougat.utils.checkpoint import get_checkpoint
CHECKPOINT = get_checkpoint('nougat')

# Download pdf from a given link
def get_pdf(pdf_link):
  # Generate a unique filename
  unique_filename = f"input/downloaded_paper_{uuid.uuid4().hex}.pdf"

  # Send a GET request to the PDF link
  response = requests.get(pdf_link)

  if response.status_code == 200:
      # Save the PDF content to a local file
      with open(unique_filename, 'wb') as pdf_file:
          pdf_file.write(response.content)
      print("PDF downloaded successfully.")
  else:
      print("Failed to download the PDF.")
  return unique_filename

# Run nougat on the pdf file
def nougat_ocr(file_name):

  # Command to run
  cli_command = [
      'nougat',
      '--out', 'output',
      'pdf', file_name,
      '--checkpoint', CHECKPOINT,
      '--markdown'
  ]

  # Run the command
  subprocess.run(cli_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  return


# predict function / driver function
def paper_read(pdf_file, pdf_link):
  if pdf_file is None:
    if pdf_link == '':
      print("No file is uploaded and No link is provided")
      return "No data provided. Upload a pdf file or provide a pdf link and try again!"
    else:
      file_name = get_pdf(pdf_link)
  else:
    file_name = pdf_file.name

  nougat_ocr(file_name)
  # Open the file for reading
  file_name = file_name.split('/')[-1][:-4]
  with open(f'output/{file_name}.mmd', 'r') as file:
      content = file.read()

  return content


# Handling examples in Gradio app
def process_example(pdf_file,pdf_link):
  ocr_content = paper_read(pdf_file,pdf_link)
  return gr.update(value=ocr_content)

# fixing the size of markdown component in gradio app
css = """
  #mkd {
    height: 500px;
    overflow: auto;
    border: 1px solid #ccc;
  }
"""
# Gradio Blocks
with gr.Blocks(css =css) as demo:
  with gr.Row():
    mkd = gr.Markdown('Upload a PDF',scale=1)
    mkd = gr.Markdown('OR',scale=1)
    mkd = gr.Markdown('Provide a PDF link',scale=1)

  with gr.Row(equal_height=True):
    pdf_file = gr.File(label='PDF📃', file_count='single', scale=1)
    pdf_link = gr.Textbox(placeholder='Enter an arxiv link here', label='PDF link🔗🌐', scale=1)

  with gr.Row():
    btn = gr.Button('Run NOUGAT🍫')
    clr = gr.Button('Clear🚿')

  output_headline = gr.Markdown("PDF converted into markup language through Nougat-OCR👇:")
  parsed_output = gr.Markdown(r'OCR Output📃🔤',elem_id='mkd', scale=1, latex_delimiters=[{ "left": r"\(", "right": r"\)", "display": False },{ "left": r"\[", "right": r"\]", "display": True }])

  btn.click(paper_read, [pdf_file, pdf_link], parsed_output )
  clr.click(lambda : (gr.update(value=None),
                      gr.update(value=None),
                      gr.update(value=None)),
             [],
             [pdf_file, pdf_link, parsed_output]
            )

demo.queue()
demo.launch(share=True)

  # gr.Examples(
  #     [["nougat.pdf", ""], [None, "https://arxiv.org/pdf/2308.08316.pdf"]],
  #     inputs = [pdf_file, pdf_link],
  #     outputs = parsed_output,
  #     fn=process_example,
  #     cache_examples=True,
  #     label='Click on any examples below to get Nougat OCR results quickly:'
  # )