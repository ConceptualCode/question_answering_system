# Author: Anthony Soronnadi

from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline
from huggingface_hub.utils._errors import RepositoryNotFoundError

class GenerativeAI:
    def __init__(self):
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')
            self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)
        except RepositoryNotFoundError:
            raise ValueError("The model gpt2 was not found. Please make sure the model identifier is correct.")
    
    def generate_answer(self, prompt):
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors='pt')
            
            if inputs.shape[1] > self.model.config.max_position_embeddings:
                raise ValueError(f"Input length ({inputs.shape[1]}) exceeds model's maximum input length ({self.model.config.max_position_embeddings}). Please shorten the prompt.")
            
            outputs = self.model.generate(
                inputs, 
                max_length=200, 
                num_return_sequences=1, 
                no_repeat_ngram_size=2, 
                early_stopping=True
            )
            response = self.tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
            return response
        except Exception as e:
            print(f"Error in generating answer: {str(e)}")
            return ""
