import glob
import pandas as pd
import matplotlib.pyplot as plt


class AeroDataset:

    def __init__(self, filepath, dataset_type):
        self.filepath = filepath
        self.dataset_type = dataset_type
        self.label = filepath

        self.df = self.load_data()

        # Calculate lift-to-drag ratio
        self.df["L_D"] = self.df["Cl"] / self.df["Cd"]

    def load_data(self):

        # XFOIL text file
        if self.dataset_type == "xfoil":

            columns = ["Alpha", "Cl", "Cd", "Cdp", "Cm", "Top_Xtr", "Bot_Xtr"]
            df = pd.read_csv(self.filepath, skiprows = 12, delim_whitespace = True, names = columns)

        # SolidWorks or published CSV file
        else:

            df = pd.read_csv(self.filepath)

            # Rename published-data columns
            # SolidWorks columns already named Alpha, Cl, Cd are unchanged
            df = df.rename(columns = { "alpha_deg": "Alpha", "alpha": "Alpha", "cl": "Cl", "cd": "Cd"})

        return df


def load_datasets():

    datasets = []

    # Find all XFOIL text files
    for file in glob.glob("*.txt"):
        datasets.append(AeroDataset(file, "xfoil"))

    # Find all CSV files
    # This includes SolidWorks and published NACA data
    for file in glob.glob("*.csv"):
        datasets.append(AeroDataset(file, "csv"))

    return datasets


def plot_results(datasets):

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    plots = [
        ("Cl", r"Lift Coefficient $C_l$", "Lift Coefficient vs Angle of Attack"),
        ("Cd", r"Drag Coefficient $C_d$", "Drag Coefficient vs Angle of Attack"),
        ("L_D", r"L/D Ratio $L/D$", "L/D Ratio vs Angle of Attack")
    ]

    for i, (column, ylabel, title) in enumerate(plots):

        for dataset in datasets:

            # XFOIL shown with dashed line
            if dataset.dataset_type == "xfoil":

                axes[i].plot(
                    dataset.df["Alpha"], 
                    dataset.df[column],
                    linestyle = "--",
                    label = dataset.label
                )

            # SolidWorks and published data shown with points
            else:

                axes[i].plot(
                    dataset.df["Alpha"],
                    dataset.df[column],
                    marker="o",
                    label=dataset.label
                )

        axes[i].set_xlabel("Angle of Attack (deg)")
        axes[i].set_ylabel(ylabel)
        axes[i].set_title(title)
        axes[i].grid(True)
        axes[i].legend()

    plt.tight_layout()
    plt.savefig("naca2412_results.png", dpi=300)
    plt.show()


# Main program
datasets = load_datasets()

plot_results(datasets)