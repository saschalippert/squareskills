import collections

import matplotlib
import matplotlib.pyplot as plt
import squarify

if __name__ == "__main__":
    skills = {
        "Java": 10,
        "Python": 2,
        "Spring": 7,
        "Hibernate": 5,
        "PyTorch": 1,
        "Oracle/SQL": 10,
        "Git": 2,
        "Subversion": 8,
        "Maven": 5,
        "Docker": 2,
        "JMS": 6,
        "JS": 2,
        "React": 1,
    }

    skills = collections.OrderedDict(sorted(skills.items(),
                                            key=lambda item: item[1],
                                            reverse=True))

    values = skills.values()

    cmap = matplotlib.cm.cividis
    mini = 0  # min(values)
    maxi = max(values)
    norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in values]

    plt.rc('font', size=14)

    dpi = 125

    fig = plt.figure(figsize=(1024 / dpi, 1024 / dpi), dpi=dpi)
    ax = fig.add_subplot()

    squarify.plot(ax=ax,
                  sizes=values,
                  label=[f"{k}" for k, v in skills.items()],
                  color=colors,
                  alpha=0.8)

    plt.axis('off')

    plt.show()
