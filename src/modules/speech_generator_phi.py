# from src.modules.paths_reference import ROOT_PATH
from modules.paths_reference import ROOT_PATH
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
set_seed(2024)


def generate_speech(model,tokenizer,prompt, max_new_tokens=120):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs,
                             do_sample=True,
                             max_new_tokens=max_new_tokens,
                             temperature=0.7,
                             top_k=50,
                             top_p=0.95,
                             no_repeat_ngram_size=2)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def load_model():
    model_checkpoint = ROOT_PATH / "models" / "phi-3-mini-speech-generator"

    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_checkpoint,
                                                 trust_remote_code=True,
                                                 torch_dtype="auto",
                                                 device_map="auto")

    model.eval()
    return model,tokenizer



# def request_speech(prompt):
#
#     model, tokenizer = load_model()
#     return generate_speech(model,tokenizer,prompt)