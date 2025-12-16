# 01Promise

# 1.Promise 中的方法

## 1.1then 方法

### 1.1.1then 方法参数

then 方法可以有两个参数，第一个参数处理 resolve 抛出的正常值，第二个参数处理 reject 抛出的异常。

```javascript
new Promise((res, rej) => {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}).then(suc => {
  console.log("suc: ", suc)
}, err => {
  console.log("err: ", err)
})

```

正常情况下只用一个参数的形式，用来处理 resolve 的正常情况，而 reject 的异常情况通常在 catch 方法中处理。

```javascript
new Promise((res, rej) => {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}).then(suc => {
  console.log("suc: ", suc)
}).catch(err => {
  console.log("err: ", err)
})

```

### 1.1.2then 方法的返回值

1. 返回 Promise

```javascript
const fun = function(res, rej) {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}
new Promise(fun)
.then(data => new Promise(fun))
.then(data => new Promise(fun))
```

每个 then 中的 data  都是上一个 then 中返回的 promise 中的 res 中抛出的值。

2. 返回字符串

```javascript
const fun = function(res, rej) {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}
new Promise(fun)
.then(data => data + " 1")
.then(data => data + " 1")
.then(data => console.log(data))
```

每个 then 中的 data 都是上一个 then 处理后的返回值。

3. 抛出异常

```javascript
const fun = function(res, rej) {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}
new Promise(fun)
.then(data => data + " 1")
.then(data => {
  throw new Error("主动抛出异常 " + data)
})
.then(data => console.log(data))
.catch(err => {
  console.log(err)
})
```

如果能走到抛出异常的 then 方法，则下面的 then 方法不会继续执行，而是直接执行 catch 方法。

## 1.2catch 方法

进入 catch 方法的两种情况：

1. 在 Promise 执行过程中通过 reject 方法返回数据
2. 在 then 方法中主动抛出异常

catch 方法不是必须的，可以在 then 中通过第二个参数进行处理异常；同时 catch 方法一般来讲只用写一个，因为以上两种情况的异常都只会就近进入一个 catch 方法中执行。

## 1.3finally 方法

无论最终执行了 then 方法，还是 catch 方法，最终都会执行到 finally 方法中。需要注意的是 finally 之后还可以继续执行 then 方法，但是这个 then 方法没有参数，即使在 finally 中有返回值也不生效。

```javascript
const fun = function(res, rej) {
  const r = Math.random()
  if (r > 0.5) {
    res("success: " + r)
  } else {
    rej ("error: " + r)
  }
}
new Promise(fun)
.then(data => data + " 1")
.then(data => data + " 1")
.then(data => console.log(data))
.catch(err => {
  console.log(err)
}).finally(() => {
  console.log("finally...")
  return "hello"
}).then((data) => {
  console.log("data: ", data)
  // data:  undefined
})
```

# 2.Promise 中的静态方法

## 2.1Promise.resolve()

返回一个带有给定值解析后的 Promise 对象：

```javascript
let p = Promise.resolve("hello world!")
p.then(data => console.log(data))
// 除非 then 中抛出异常否则不会进入 catch
.catch(err => console.log(err))
```

## 2.2Promise.reject()

返回一个带有 reject 原因的 Promise 对象：

```javascript
let p = Promise.reject("hello bitch!")
p
// 不会进入 then 直接到 catch
.then(data => console.log(data))
.catch(err => console.log(err))
```

## 2.3Promise.all()

接收多个 Promise 对象，等待所有的 Promise 对象执行完成之后返回一个 Promise 实例。

如果所有 Promise 对象的 then 方法正常执行则才会进入 Promise 实例的 then 方法中，方法参数为所有 Promise 对象 then 的返回值；反之，只要有一个 Promise 对象执行了 reject 方法则直接进入 catch 方法中。

**全部 then 方法正常执行：**

```javascript
let p1 = Promise.resolve("hello world1!")
let p2 = Promise.resolve("hello world2!")
let p3 = Promise.resolve("hello world3!")
let p4 = Promise.resolve("hello world4!")
Promise.all([p1, p2, p3, p4])
.then(data => console.log(data))
// [ 'hello world1!', 'hello world2!', 'hello world3!', 'hello world4!' ]
.catch(err => console.log(err))
```

**存在 Promise 对象执行了 reject 方法：**

```javascript
let p1 = Promise.resolve("hello world1!")
let p2 = Promise.resolve("hello world2!")
let p3 = Promise.resolve("hello world3!")
let p4 = Promise.resolve("hello world4!")
let p5 = Promise.reject("hello bitch5!")

Promise.all([p1, p2, p3, p4, p5])
// 不执行 then
.then(data => console.log(data))
.catch(err => console.log(err))
```

## 2.4Promise.race()

方法接收多个 Promise 对象，只要有一个 Promise 对象执行了 resolve 或者 reject 就返回一个 Promise 实例；可以通过 then 或 catch 来处理最快的 Promise 对象的 resolve 或 reject 参数。

```javascript
let p1 = new Promise((res, rej) => {
  setTimeout(() => {
    res(200)
  }, 200)
})
let p2 = new Promise((res, rej) => {
  setTimeout(() => {
    res(300)
  }, 300)
})
let p3 = new Promise((res, rej) => {
  setTimeout(() => {
    rej(400)
  }, 400)
})

Promise.race([p1, p2, p3])
.then(data => console.log(data))
// 200
.catch(err => console.log(err))
```

注意：虽然这个方法选择了最快执行完成的 Promise 对象，但是其他 Promise 对象的方法仍在执行，并不会中断直接舍弃。
