# MatheUI-2.0
little funny games

/pypi/v/matheUI-backend

## set-up package

install the package to your activated virtual environment

```
pip install matheUI-backend
```

Now you can use the package. e.g.:

```
from matheUI_backend import AgentUndercover

auc = AgentUndercover()
auc.generate_round(player_number=7, spy_number=2, places_groups="standard")
```

--> in the '[examples](https://github.com/Priapos1004/MatheUI-2.0_backend/tree/main/examples)' folder you can find notebooks with code snippets that explain the usage of the package
