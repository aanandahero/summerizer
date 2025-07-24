from transformers import pipeline

# Load summarizer pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Long text to summarize
text = """
DevOps is a set of practices that combines software development and IT operations. 
It aims to shorten the systems development life cycle and provide continuous delivery with high software quality. 
DevOps is complementary with Agile software development; several DevOps aspects came from Agile methodology. 
DevOps helps increase an organization's speed to deliver applications and services. 
It allows organizations to serve their customers better and compete more effectively in the market.
"""

# Summarize
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

print("📄 Summary:\n", summary[0]['summary_text'])
