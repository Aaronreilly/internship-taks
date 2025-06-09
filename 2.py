import matplotlib.pyplot as plt

def plot_data():
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 56, 78]
    plt.bar(categories, values, color='skyblue')
    plt.title('Sample Data Visualization')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

plot_data()
