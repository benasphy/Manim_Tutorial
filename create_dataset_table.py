import matplotlib.pyplot as plt
import numpy as np

# Data
sizes = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
prices = [150, 200, 250, 175, 300, 225, 275, 250, 300, 350]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')

# Create the table
table_data = [['Size (1000 sqft)', 'Price ($1000s)']] + list(zip(sizes, prices))
table = ax.table(
    cellText=table_data,
    loc='center',
    cellLoc='center',
    colWidths=[0.3, 0.3]
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 2)

# Highlight header
for (i, j), cell in table.get_celld().items():
    if i == 0:  # Header row
        cell.set_facecolor('#4a6ea9')
        cell.set_text_props(color='white', weight='bold')
    cell.set_linewidth(0.5)

# Save the figure
plt.tight_layout()
plt.savefig('house_price_dataset.png', dpi=150, bbox_inches='tight', pad_inches=0.5)
print("Dataset table saved as 'house_price_dataset.png'")
