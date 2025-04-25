# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set plot styles
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the cleaned dataset
df = pd.read_csv('titanic_cleaned.csv')

# Step 1: Summary Statistics
print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Step 2: Histograms and Boxplots
# Histogram - Age
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Normalized Age')
plt.show()

# Histogram - Fare
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Normalized Fare')
plt.show()

# Boxplot - Age
sns.boxplot(x=df['Age'])
plt.title('Boxplot of Age')
plt.show()

# Boxplot - Fare
sns.boxplot(x=df['Fare'])
plt.title('Boxplot of Fare')
plt.show()

# Step 3: Correlation Matrix
corr = df.corr()
print("\nCorrelation Matrix:")
print(corr)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Step 4: Pairplot
sns.pairplot(df, hue='Survived', vars=['Age', 'Fare', 'Pclass', 'Sex'])
plt.suptitle("Pairplot of Features Colored by Survival", y=1.02)
plt.show()

# Step 5: Countplots for Categorical Inferences
# Survived Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Survived by Sex
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Gender")
plt.xlabel("Sex (0 = Male, 1 = Female)")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.show()

# Survived by Pclass
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival Count by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title='Survived')
plt.show()
