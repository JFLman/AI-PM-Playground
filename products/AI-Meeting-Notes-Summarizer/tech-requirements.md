# Technical Requirements: AI Meeting Notes Summarizer

High-level specs to guide development.

## Inputs
- Text files (<10MB) or audio recordings (<1 hour).
- Supported formats: .txt, .docx, .mp3, .wav.

## Processing
- NLP Model: Pre-trained model (e.g., BERT, GPT-3) fine-tuned on meeting transcripts.
- Key Features:
  - Extract action items (e.g., “Mike will research by Friday”).
  - Identify decisions (e.g., “Team agreed to prioritize bugs”).
  - Summarize in <100 words.
- Latency: <30 seconds for 500-word input.

## Outputs
- Summary in Markdown or plain text.
- Optional: Highlighted action items in bold.

## Constraints
- Accuracy: >90% key point capture.
- Cost: API usage < $0.50 per summary.
- Privacy: No storage of raw notes post-processing.

## Risks
- AI misinterpreting context (mitigate with user feedback loop).
- Bias in model outputs (test diverse meeting types).
