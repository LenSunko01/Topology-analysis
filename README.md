# Topology-analysis

Граф отражает поток управления в коде на Python.  
Вершины графа - место, где может находиться потом управления. Из каждой вершины выходит одно или несколько ребер, которые обозначают переходы.  
Например, если есть ветвление вида:

```
if x > 3:
  y = 2
else:
  y = 1
```

то из вершины if x > 3 будет выходить два ребра в вершины y = 2 и y = 1.

Ребро пунктирное, если оно ведет в состояние ошибки (считаем, что ошибка может произойти на каждом шаге и такое ребро ведет из каждой вершины), иначе сплошное.
