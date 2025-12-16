# Zookeeper

# 1.watch 的各类事件

## 1.1父节点 NodeCreated 事件

- `stat /abc watch` 查看一个未创建节点的状态时添加 watch 事件，当该节点创建时会触发对应事件

## 1.2父节点 NodeDataChanged 事件

- `get /abc watch` 查看父节点的值时添加 watch 事件，当该节点的数据被重新 set 时会触发对应事件

## 1.3父节点 NodeDeleted 事件

- `get /abc watch` 查看父节点的值时添加 watch 事件，当该节点被 delete 时会触发对应事件

## 1.4父节点 NodeChildrenChanged 事件

- `ls /abc watch` 查看父节点的子节点时添加 watch 事件，当在父节点下创建子节点或删除子节点时会触发该事件
