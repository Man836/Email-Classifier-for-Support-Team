# Email Classifier & PII Masker

This space allows users to input email content. It performs the following:
- Masks Personally Identifiable Information (PII) using spaCy and Regex.
- Classifies the email into categories using a trained ML model.

## How to Use
- Paste an email in the textbox.
- Get back a masked version, list of detected PII entities, and classification.

## Model
- Trained using scikit-learn on support request data.
- PII masking combines spaCy NER and Regex.

## Author
Manisha M Phulanekar

