import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

iris = sns.load_dataset("iris")

print(iris.head())

species_int = []
for row in iris.values:
    match row[4]:
        case "setosa":
            species_int.append(1)
        case "versicolor":
            species_int.append(2)
        case "virginica":
            species_int.append(3)

species_int = pd.DataFrame(species_int)
print(species_int.head())

data = iris[["sepal_length", "petal_length"]]

data["species"] = species_int

print(data.head())
print(data.shape)

# data_df = data[(data['species'] == 1) | (data['species'] == 2)]
# print(data_df.shape)

# data_of_setosa = data[data['species'] == 1]
# data_of_versicolor = data[data['species'] == 2]


# plt.scatter(data_of_setosa['sepal_length'], data_of_setosa['petal_length'])
# plt.scatter(data_of_versicolor['sepal_length'], data_of_versicolor['petal_length'])
# # plt.show()

# X = data_df[['sepal_length', 'petal_length']]
# y = data_df['species']

# from sklearn.tree import DecisionTreeClassifier

# model = DecisionTreeClassifier()
# model.fit(X, y)

# x1_p = np.linspace(min(data_df['sepal_length']), max(data_df['sepal_length']))
# x2_p = np.linspace(min(data_df['petal_length']), max(data_df['petal_length']))

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# print(X1_p.shape)

# X_p = pd.DataFrame(np.vstack([X1_p.ravel(), X2_p.ravel().T]), columns=['sepal_length'])

# print(X_p.head())

# y_p = model.predict(X_p)

# plt.contourf(X1_p, X2_p, y_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 1.5, 2.5])

# plt.show()


# data_df = data[(data["species"] == 2) | (data["species"] == 3)]
# print(data_df.shape)

# data_of_virginica = data[data["species"] == 3]
# data_of_versicolor = data[data["species"] == 2]

# data_of_virginica_A = data_of_virginica.iloc[:25, :]
# data_of_virginica_B = data_of_virginica.iloc[25:, :]

# data_of_versicolor_A = data_of_versicolor.iloc[:25, :]
# data_of_versicolor_B = data_of_versicolor.iloc[25:, :]

# data_df_A = pd.concat([data_of_virginica_A, data_of_versicolor_A], ignore_index=True)
# data_df_B = pd.concat([data_of_virginica_B, data_of_versicolor_B], ignore_index=True)


# from sklearn.tree import DecisionTreeClassifier

# max_depth = [1, 3, 5, 7]

# fig, ax = plt.subplots(2, 4, sharex="col", sharey="row")

# X = data_df_A[["sepal_length", "petal_length"]]
# y = data_df_A["species"]

# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]))
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]))

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# print(X1_p.shape)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )


# j = 0
# for md in max_depth:
#     model = DecisionTreeClassifier(max_depth=md)
#     model.fit(X, y)

#     y_p = model.predict(X_p)
#     ax[0, j].scatter(
#         data_of_virginica_A["sepal_length"], data_of_virginica_A["petal_length"]
#     )
#     ax[0, j].scatter(
#         data_of_versicolor_A["sepal_length"], data_of_versicolor_A["petal_length"]
#     )

#     ax[0, j].contourf(
#         X1_p, X2_p, y_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 2.5, 3.5]
#     )
#     j += 1
# print(X_p.head())

# y_p = model.predict(X_p)

# X = data_df_B[["sepal_length", "petal_length"]]
# y = data_df_B["species"]

# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]))
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]))

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# print(X1_p.shape)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )


# j = 0
# for md in max_depth:
#     model = DecisionTreeClassifier(max_depth=md)
#     model.fit(X, y)

#     y_p = model.predict(X_p)
#     ax[1, j].scatter(
#         data_of_virginica_A["sepal_length"], data_of_virginica_A["petal_length"]
#     )
#     ax[1, j].scatter(
#         data_of_versicolor_A["sepal_length"], data_of_versicolor_A["petal_length"]
#     )

#     ax[1, j].contourf(
#         X1_p, X2_p, y_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 2.5, 3.5]
#     )
#     j += 1
# print(X_p.head())

# y_p = model.predict(X_p)

# plt.show()


# Bagging
# Random forest


# data_of_setosa = data[data["species"] == 1]
# data_of_versicolor = data[data["species"] == 2]
# data_of_virginica = data[data["species"] == 3]

# X = data[["sepal_length", "petal_length"]]
# y = data["species"]

# max_depth = [1, 3, 5, 7]

# fig, ax = plt.subplots(1, 3, sharex="col", sharey="row")

# ax[0].scatter(data_of_setosa['sepal_length'], data_of_setosa['petal_length'])
# ax[0].scatter(data_of_versicolor['sepal_length'], data_of_versicolor['petal_length'])
# ax[0].scatter(data_of_virginica['sepal_length'], data_of_virginica['petal_length'])

# ax[1].scatter(data_of_setosa['sepal_length'], data_of_setosa['petal_length'])
# ax[1].scatter(data_of_versicolor['sepal_length'], data_of_versicolor['petal_length'])
# ax[1].scatter(data_of_virginica['sepal_length'], data_of_virginica['petal_length'])

# ax[2].scatter(data_of_setosa['sepal_length'], data_of_setosa['petal_length'])
# ax[2].scatter(data_of_versicolor['sepal_length'], data_of_versicolor['petal_length'])
# ax[2].scatter(data_of_virginica['sepal_length'], data_of_virginica['petal_length'])

# X = data[["sepal_length", "petal_length"]]
# y = data["species"]

# x1_p = np.linspace(min(data["sepal_length"]), max(data["sepal_length"]))
# x2_p = np.linspace(min(data["petal_length"]), max(data["petal_length"]))

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# print(X1_p.shape)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )

# from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
# from sklearn.tree import DecisionTreeClassifier

# model1 = RandomForestClassifier(max_depth=6)
# model1.fit(X, y)

# y1_p = model1.predict(X_p)

# ax[0].contourf(
#     X1_p, X2_p, y1_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5]
# )

# model2 = DecisionTreeClassifier(max_depth=6)
# bagging = BaggingClassifier(model2, n_estimators=10, max_samples=0.6, random_state=1)
# bagging.fit(X, y)

# y2_p = bagging.predict(X_p)

# ax[1].contourf(
#     X1_p, X2_p, y2_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5]
# )

# model3 = RandomForestClassifier(max_depth=6, n_estimators=10, max_samples=0.6, random_state=1)
# model3.fit(X, y)

# y3_p = model3.predict(X_p)

# ax[2].contourf(
#     X1_p, X2_p, y3_p.reshape(X2_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5]
# )

# plt.show()

# # + простые модели + быстро решаются + параллелизм
# # + голосование
# # + непараметрическая - эффективная работа с данными
# # - осмысленные выводы сложно сделать


data = iris[["sepal_length", "petal_length", "species"]]

data_setosa = data[data["species"] == "setosa"]
data_setosa = data_setosa.drop(columns="species")

print(data_setosa.head())

X = data_setosa["sepal_length"]
Y = data_setosa["petal_length"]


from sklearn.decomposition import PCA

pca = PCA(n_components=2)
new_data = pca.fit_transform(data_setosa)

print("l")

print(pca.components_)

print(pca.mean_)

print(pca.explained_variance_)

plt.scatter(X, Y)
plt.scatter(pca.mean_[0], pca.mean_[1])

plt.plot(
    [
        pca.mean_[0],
        pca.mean_[0] + pca.components_[0][0] * np.sqrt(pca.explained_variance_[0]),
    ],
    [
        pca.mean_[1],
        pca.mean_[1] + pca.components_[0][1] * np.sqrt(pca.explained_variance_[0]),
    ],
)

plt.plot(
    [
        pca.mean_[0],
        pca.mean_[0] + pca.components_[1][0] * np.sqrt(pca.explained_variance_[1]),
    ],
    [
        pca.mean_[1],
        pca.mean_[1] + pca.components_[1][1] * np.sqrt(pca.explained_variance_[1]),
    ],
)


pca1 = PCA(n_components=1)
X_pca1 = pca1.fit_transform(data_setosa)

print(data_setosa.shape)
print(X_pca1.shape)


X_new = pca1.inverse_transform(X_pca1)

plt.scatter(X_new[:, 0], X_new[:, 1])

plt.show()

# - аномальные значения
