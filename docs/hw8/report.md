# Поиск по ФИО 

### Без индексов

![img.png](img.png)

![img_1.png](img_1.png)

![img_2.png](img_2.png)

### С индексами

С помощью инструмента из первой домашки по индексам и по примеру семинара добавил индексы:
```sql
CREATE INDEX "~users-fcc8a6b8"
  ON users((name::text) text_pattern_ops, id);
CREATE INDEX users_name_trgm_idx ON users USING GIN (name gin_trgm_ops);
```

![img_3.png](img_3.png)

![img_4.png](img_4.png)

![img_5.png](img_5.png)


# Поиск по сообщениям у друзей пользователя

### Без индексов

![img_6.png](img_6.png)

Полнотекстовый

![img_7.png](img_7.png)

### С индексами

По документации постгреса добавил индекс для полнотекстового поиска + решил попробовать добавить gin_trgm_ops

```sql
CREATE INDEX messages_text_trgm_idx ON messages USING GIN (text gin_trgm_ops);
CREATE INDEX messages_text_ts_idx ON messages USING GIN (to_tsvector('russian', text));
```

![img_8.png](img_8.png)

![img_9.png](img_9.png)


## Выводы

Используя встроенные инструменты и расширения Postgres кажется вполне можно добиться приемлимых результатов для поиска по небольшому объему текстовой информации, в иных случаях лучше использовать специализированные инструменты, например Elasticsearch.