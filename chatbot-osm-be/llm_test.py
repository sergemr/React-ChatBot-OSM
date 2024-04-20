import numpy as np
from llama_cpp import Llama
from llm_adapter import llm_chatbot_response_vs
# Load the Llama model
llm = Llama(model_path="./llm-codellama-instruct.gguf",  # Use llm-gemma.gguf for the Gemma model
            chat_format="llama-2",
            n_ctx=124,
            n_threads=6,
            n_gpu_layers=2)

# Function to extract embeddings for a given text


def test_get_embeddings(text):
    print("@@text")
    print(text)
    tokenized_text = llm.tokenize(text.encode('utf-8'))
    embeddings = llm.get_contextual_embeddings([tokenized_text])
    return embeddings


# Original text
original_text = "The complete history of the Old Republic would fill a thousand libraries. Some events and some sacrifices have become legend, passed from generation to generation.As with any history that extends back for millennia, details and facts become blurred by time. Events that took place so long ago become shrouded in contradictions and myth. The exact sequence and some of the names may not be entirely accurate, but without question the overall conflicts are real.Pre-Republic history is incredibly ancient and notoriously difficult to research. At some point in this ancient era the Corellian system was artificially created, providing evidence that our region of space was once visited by stunningly powerful alien architects, who may also have been responsible for the unlikely cluster of black holes near Kessel known as the Maw. On Coruscant, prime planet of what would later be known as the Core Worlds, two armies—the Taungs and the Battalions of Zhell—clashed in a legendary battle. The Zhell were defeated when a sudden volcanic eruption smothered their encampment, and the towering plume of black ash loomed over the Taung army for two years. The awed Taungs took the name Warriors of the Shadow—or, in the ancient tongue, Dha Werda Verda. Their story is recounted in the epic poem of the same name. The original site of this battlefield is now buried beneath the skyscrapers of Imperial City.Xim the Despot is the most celebrated pre-Republic conqueror of all. In the remote region now known as the Tion Hegemony, Xim gathered vast armies under his banner, including a legion of unstoppable war droids—the earliest-known combat automatons. Xim's glorious empire spread to encompass hundreds of thousands of worlds in the vicinity of the Tion. The warlord miscalculated, however, when he tried to expand into Hutt Space. The Hutts had built up their own formidable star empire, and they fiercely opposed Xim for possession of the Si'klaata Cluster. Two exhausting but inconclusive battles were fought on the planet Vontor. In the third such confrontation, Xim's war droids were opposed by the Hutts' latest conscripts—a horde of fighters from the Nikto, Vodran, and Klatoo"
# Split the text into individual messages
messages = original_text.split('\n')

# Get embeddings for each message
embeddings = [test_get_embeddings(message) for message in messages]

# Pass messages and embeddings to the llm_chatbot_response_vs function
response, status_code = llm_chatbot_response_vs(
    {'messages': messages, 'temperature': 0.7}, embeddings)
print(response)

print('@@@this is a test@@@')
