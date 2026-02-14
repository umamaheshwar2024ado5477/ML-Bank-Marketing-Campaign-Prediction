# BITS Lab Screenshot Guide

## What to Capture in Your Screenshot

Your screenshot should clearly show:

1. **Evidence of BITS Virtual Lab**:
   - BITS Lab logo or identifier visible
   - Lab environment taskbar or window

2. **Your Work**:
   - Terminal/command prompt showing:
     - The training command: `python train_model.py`
     - Model training progress output
     - Final evaluation results table
   - OR IDE (VS Code/PyCharm) showing:
     - Your code files open
     - Terminal output within IDE

3. **Timestamp/Date**:
   - System clock showing current date/time
   - Or terminal output with timestamp

4. **Model Results Visible**:
   - The evaluation metrics table showing all 6 models
   - Clear view of Accuracy, AUC, Precision, Recall, F1 Score, MCC

## How to Take Screenshot

### On Windows (BITS Lab):
1. **Full Screen**: Press `PrtSc` (Print Screen) key
2. **Active Window**: Press `Alt + PrtSc`
3. **Snipping Tool**: 
   - Press `Windows + Shift + S`
   - Select area to capture
   - Screenshot copied to clipboard

### Save Screenshot:
1. Open Paint or any image editor
2. Paste (Ctrl + V)
3. Save as PNG or JPG
4. Name it: `BITS_Lab_Execution_Screenshot.png`

## Recommended Screenshot Composition

```
┌─────────────────────────────────────────────────────┐
│ BITS Virtual Lab Environment        [X] 1:45 PM     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Terminal / Command Prompt                          │
│  ┌──────────────────────────────────────────────┐  │
│  │ C:\UmaMahesh\ML_Assignment_2> python         │  │
│  │ train_model.py                               │  │
│  │                                              │  │
│  │ Loading dataset...                          │  │
│  │ Categorical columns: ['job', 'marital',     │  │
│  │ 'education', ...]                           │  │
│  │ Numerical columns: ['age', 'balance', ...]  │  │
│  │                                              │  │
│  │ Training models...                          │  │
│  │ Training Logistic Regression...             │  │
│  │ Training Decision Tree...                   │  │
│  │ Training KNN...                             │  │
│  │ Training Naive Bayes...                     │  │
│  │ Training Random Forest...                   │  │
│  │ Training XGBoost...                         │  │
│  │                                              │  │
│  │ Evaluation Results:                         │  │
│  │             Model  Accuracy    AUC  ...     │  │
│  │ 0  Logistic Reg..  0.898706  0.904  ...    │  │
│  │ 1  Decision Tree   0.873051  0.707  ...    │  │
│  │ 2  KNN            0.898485  0.851  ...     │  │
│  │ 3  Naive Bayes    0.845848  0.809  ...    │  │
│  │ 4  Random Forest  0.905562  0.927  ...    │  │
│  │ 5  XGBoost        0.908769  0.931  ...    │  │
│  │                                              │  │
│  │ Models and results saved.                   │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## Alternative: Multiple Screenshots

If one screenshot can't capture everything, take 2-3 screenshots showing:

1. **Screenshot 1**: BITS Lab environment with your project folder open
2. **Screenshot 2**: Training command and model training progress
3. **Screenshot 3**: Final evaluation results table

Then combine them in a single image using Paint/PowerPoint or include all in PDF.

## Common Mistakes to Avoid

❌ **Don't**:
- Take generic screenshots without BITS Lab identifiers
- Crop out important information (date, time, environment)
- Submit blurry or unreadable screenshots
- Take screenshot of just code without execution proof

✅ **Do**:
- Ensure BITS Lab environment is clearly visible
- Capture the complete model evaluation results
- Make sure text is readable
- Include timestamp/date information
- Show the actual execution, not just code

## After Taking Screenshot

1. Save with descriptive name: `BITS_Lab_Screenshot.png`
2. Verify it's clear and readable
3. Insert into your PDF submission
4. Add caption: "Model training and evaluation executed on BITS Virtual Lab"

## Size and Format

- **Format**: PNG or JPG
- **Size**: Keep under 5MB for PDF submission
- **Resolution**: High enough to read terminal text clearly
- If too large, use Windows Photos app to compress

---

**Remember**: The screenshot proves you executed the assignment on BITS Lab as required for the 1 bonus mark!
