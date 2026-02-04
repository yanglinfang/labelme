# Task: Add Quick Label Buttons for Rectangle Annotation

## Context
This labelme instance is being used for **litter detection labeling** as part of an active learning pipeline. The workflow involves:
1. Model predicts bounding boxes on images
2. Human reviews/corrects predictions in labelme
3. Human adds missed objects (especially occluded litter in grass)

**Problem:** When adding new rectangle annotations, the user must manually type or select the label from a dropdown. This is slow and error-prone for repetitive labeling tasks.

## Requested Feature
Add **quick label buttons** to the toolbar or sidebar that allow one-click rectangle creation with a pre-defined label.

### Use Case
For the litter detection project, we have 4 classes:
- **Grabber** (class 0) - Green
- **Litter** (class 1) - Red
- **CollectionBag** (class 2) - Blue
- **DataCollector** (class 3) - Orange

The labeler should be able to:
1. Click a "Litter" button in the toolbar
2. Draw a rectangle on the image
3. The rectangle is automatically labeled "Litter" without showing the label dialog

### Implementation Suggestions

**Option A: Toolbar Quick Buttons**
Add buttons to the toolbar that set a "current label" mode:
- When clicked, enter "draw rectangle with label X" mode
- After drawing, automatically assign the label without dialog
- Visual indicator showing which label mode is active

**Option B: Keyboard Shortcuts**
Add keyboard shortcuts (e.g., 1, 2, 3, 4) that:
- Enter rectangle mode with a pre-assigned label
- Press 1 → draw rectangle → auto-label as "Grabber"
- Press 2 → draw rectangle → auto-label as "Litter"

**Option C: Label Palette Sidebar**
Add a sidebar with clickable label buttons:
- Click label → draw shape → auto-assigned
- Similar to how Photoshop's color palette works

### Files to Modify

Based on my analysis of the codebase:

1. **`labelme/app.py`** - Main application, add toolbar buttons and shortcuts
2. **`labelme/widgets/canvas.py`** - Canvas drawing, handle auto-labeling mode
3. **`labelme/widgets/label_dialog.py`** - May need to bypass for quick labels
4. **`labelme/config/__init__.py`** - Add config for quick label definitions

### Configuration

The quick labels should be configurable. Add to `config/default_config.yaml`:
```yaml
quick_labels:
  - name: Grabber
    shortcut: "1"
    color: [0, 255, 0]
  - name: Litter
    shortcut: "2"
    color: [255, 0, 0]
  - name: CollectionBag
    shortcut: "3"
    color: [0, 0, 255]
  - name: DataCollector
    shortcut: "4"
    color: [255, 165, 0]
```

Or via command line:
```bash
labelme --quick-labels Grabber,Litter,CollectionBag,DataCollector
```

### Acceptance Criteria

1. User can draw rectangles with pre-defined labels without opening label dialog
2. Keyboard shortcuts work (1-4 for the 4 classes)
3. Visual indicator shows current label mode
4. Feature is configurable (not hardcoded)
5. Works alongside existing manual labeling workflow

### Priority
**HIGH** - This is blocking an active learning pipeline for litter detection model improvement.

---

## Contact
This task was created by the Claude agent working in `D:\Users\Lin\Documents\Git\ClipOnAiML`.
The feature is needed for the active learning notebook: `notebooks/active_learning_test.ipynb`
