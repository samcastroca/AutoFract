# 🦴 AutoFract — Assisted Fracture Detection in Radiographs

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://autofract.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8s-00ADEF?logo=ultralytics&logoColor=white)](https://docs.ultralytics.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **AutoFract** is an AI-powered web application for automated bone fracture detection in musculoskeletal radiographs, designed to support radiologists and clinicians in faster, more accurate diagnoses.

---

## 📌 Overview

Early and accurate detection of bone fractures is critical for proper patient treatment. Radiologists can face challenges when interpreting low-quality images or subtle fracture cases. AutoFract addresses this by leveraging a fine-tuned **YOLOv8s** object detection model to automatically localize fractures in X-ray images, reducing diagnostic time and the risk of missed findings.

This project was developed as part of the *Data Analytics Integrator Project* by **Samuel Castro Carmona** and **Sofía Marín Franco**.

---

## 🚀 Live Demo

Try the application here: [https://autofract.streamlit.app/](https://autofract.streamlit.app/)

Upload any musculoskeletal radiograph (hand, shoulder, hip, or leg) and the model will detect and localize fractures with bounding box predictions and confidence scores.

---

## 🧠 Model & Dataset

The model was trained on the **FracAtlas** dataset — a publicly available collection of 4,083 musculoskeletal X-ray images (717 fractured, 922 fracture instances) annotated by 2 expert radiologists and an orthopedic surgeon, covering hand, shoulder, hip, and leg regions.

> Abedeen, I., Rahman, M. A., Prottyasha, F. Z., Ahmed, T., Chowdhury, T. M., & Shatabda, S. (2023). **FracAtlas: A Dataset for Fracture Classification, Localization and Segmentation of Musculoskeletal Radiographs**. *Scientific Data, 10*, 521. [https://doi.org/10.1038/s41597-023-02432-4](https://doi.org/10.1038/s41597-023-02432-4)

The dataset is available at Figshare: [https://doi.org/10.6084/m9.figshare.22363012](https://doi.org/10.6084/m9.figshare.22363012)

---

## 📊 Performance

The model was trained using data augmentation to address class imbalance, and evaluated on a held-out test set. Results significantly exceeded the baseline reported in the FracAtlas paper:

| Metric | FracAtlas Paper (baseline) | AutoFract (test set) |
|---|---|---|
| Precision | 80.7% | **95.5%** |
| Recall | 47.3% | **90.9%** |
| mAP@0.5 | 56.2% | **94.5%** |

The F1-Confidence curve peaks at **0.91** at a confidence threshold of **0.445**, indicating robust detection performance across a wide operating range.

---

## ⚙️ Methodology

The development pipeline consisted of the following steps:

1. **Image preprocessing** — normalization and resizing of radiograph images
2. **Class balancing** — data augmentation applied to the minority (fractured) class
3. **Train/validation/test split** — stratified partitioning of the dataset
4. **Model training** — fine-tuning YOLOv8s for fracture object detection
5. **Evaluation** — assessment of the best checkpoint on the test set

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Web app | [Streamlit](https://streamlit.io/) |
| Object detection | [Ultralytics YOLOv8](https://docs.ultralytics.com/) |
| Image processing | [OpenCV](https://opencv.org/), [Pillow](https://pillow.readthedocs.io/) |
| Language | Python 3.x |

---

## 📁 Repository Structure

```
AutoFract/
├── AutoFract/          # Main application source code
├── requirements.txt    # Python dependencies
├── packages.txt        # System-level packages
└── README.md
```

---

## 🔧 Local Setup

```bash
# Clone the repository
git clone https://github.com/samcastroca/AutoFract.git
cd AutoFract

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run AutoFract/app.py
```

---

## 💡 What This Solves

- **Reduced diagnostic time** — automates fracture detection so specialists can focus on complex cases
- **Greater accuracy** — lowers the risk of misdiagnosis by providing a second-opinion AI layer
- **Workflow optimization** — helps hospitals and clinics prioritize urgent cases more efficiently

---

## 👥 Authors

- **Samuel Castro Carmona** — [@samcastroca](https://github.com/samcastroca)
- **Sofía Marín Franco** - [@somarinf](https://github.com/somarinf)

*Data Analytics Integrator Project*



---

> ⚠️ **Disclaimer:** AutoFract is a research and educational tool. It is not intended to replace professional medical diagnosis. Always consult a qualified radiologist or physician for clinical decisions.
