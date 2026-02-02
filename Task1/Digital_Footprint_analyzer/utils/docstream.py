# Generator function to stream documents line by line
def stream_documents(lines):
    # Yield one line at a time instead of loading everything into memory
    for line in lines:
        yield line
