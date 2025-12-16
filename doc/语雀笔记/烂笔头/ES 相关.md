# ES 相关

## 1.查询并更新

```json
POST /call-cajr-lb1001/_update_by_query
{
  "script": {
    "source": "ctx._source.tenantId = params.new_value;ctx._source.orgCode = params.new_value",
    "params": {
      "new_value": "af8a99be-3f5e-4c68-8686-b2e2922bef11"
    }
  },
  "query": {
    "match_all": {}
  }
}
```

## 2.更新一个文档

```json
POST /call-cajr-lb1001/_update/41c77afb-e486-44a6-956d-05be0067f6da
{
  "doc": {
    "orgCode": "af8a99be-3f5e-4c68-8686-b2e2922bef11a"
  }
}
```
