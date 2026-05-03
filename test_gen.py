from transformers import pipeline

def test_generation():
    print("Loading model...")
    generator = pipeline('text-generation', model='gpt2')
    print("Generating text...")
    prompt = "Artificial Intelligence in Education"
    output = generator(prompt, max_length=50, num_return_sequences=1)
    print("\n--- Output ---")
    print(output[0]['generated_text'])

if __name__ == "__main__":
    test_generation()
