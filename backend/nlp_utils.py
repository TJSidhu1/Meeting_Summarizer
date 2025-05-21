import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
# summarizer = pipeline("summarization")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

decision_keywords = [
    "agreed to", "decided to", "concluded that", "approved",
    "settled on", "we will", "we shall", "it was decided", "it was agreed"
]

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# def extract_action_items(text):
#     doc = nlp(text)
#     actions = []
#     for sent in doc.sents:
#         subj, verb, obj = None, None, None
#         for token in sent:
#             if "subj" in token.dep_ and subj is None:
#                 subj = token.text
#             elif token.pos_ == "VERB" and verb is None:
#                 verb = token.lemma_
#             elif "obj" in token.dep_ and obj is None:
#                 obj = token.text
#         if subj and verb:
#             action = f"{subj} {verb}"
#             if obj:
#                 action += f" {obj}"
#             actions.append(action)
#     return actions

def extract_action_items(text):
    doc = nlp(text)
    actions = []
    for sent in doc.sents:
        # We look for sentences with imperative verbs or modal verbs indicating actions
        if any(token.tag_ in ("VB", "VBP") for token in sent):  # simple verb check
            actions.append(sent.text.strip())
    return actions


# def extract_decisions(text):
#     doc = nlp(text)
#     decisions = []
#     for sent in doc.sents:
#         if any(phrase in sent.text.lower() for phrase in decision_keywords):
#             decisions.append(sent.text.strip())
#     return decisions

def extract_decisions(text):
    doc = nlp(text)
    decisions = []
    for sent in doc.sents:
        sentence_text = sent.text.lower()
        if any(phrase in sentence_text for phrase in decision_keywords):
            decisions.append(sent.text.strip())
    return decisions


def process_transcript(text):
    summary = summarize_text(text)
    actions = extract_action_items(text)
    decisions = extract_decisions(text)
    return summary, actions, decisions
