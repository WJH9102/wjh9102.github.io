---
typora-copy-images-to: images
---

## Tinymce使用教程

#### 1.安装Tinymce

`npm install @tinymce/tinymce-vue -S`

`npm install tinymce -S`

#### 2.下载语言包并引入

1. 下载语言包，地址：[中文包](https://www.tiny.cloud/get-tiny/language-packages/)
2. 在vue中引入，将`zh_CN.js`复制到`public`或者`static`下

#### 3.自己封装组件

1. 导入相关js和css

   - `import tinymce from 'tinymce/tinymce'`
   - `import 'tinymce/themes/silver/theme'`
   - `import '../../../public/tinymce/zh_CN'`
   - `@import url('~tinymce/skins/ui/oxide/skin.min.css');`

2. 初始化组件（基本完成，可以使用）

   ~~~html
   <template>
     <div id='tinymce'>
       <section class="tinymce-editor"></section>
     </div>
   </template>
   ~~~

   ~~~js
   data () {
       return {
         initObj: {
           selector: '.tinymce-editor',
           language: 'zh_CN'
         }
       }
   },
   mounted() {
       tinymce.init(this.initObj)
   }
   
   ~~~

3. 按需自定义工具栏和导入插件

   - 导入一些插件

     ```
     import 'tinymce/plugins/preview/plugin'
     import 'tinymce/plugins/image/plugin'
     import 'tinymce/plugins/link/plugin'
     ```

   - 在`initObj`中使用

     ~~~js
     initObj: {
             selector: '.tinymce-editor',
             language: 'zh_CN',
             toolbar1: 'undo redo | styleselect | bold italic | link image | alignleft aligncenter alignright | outdent indent | preview',
             plugins: 'preview image link'
     }
     ~~~

4. 一些回调方法（都需要在`initObj`中注册使用）

   - 监听初始化完成事件

     ~~~js
     setup: (editor) => {
         editor.on('init', (e) => {
             editor.setContent(this.value)
         })
     }
     ~~~

   - 监听`input` 和 `change` 事件实时更新value的值

     ~~~js
     init_instance_callback: (editor) => {
         editor.on('input', (e) => {
             this.$emit('input', e.target.innerHTML)
         })
         editor.on('change', (e) => {
             this.$emit('input', e.level.content)
         })
     }
     ~~~

   - 本地图片上传方法回调

     ~~~js
     images_upload_handler (blobInfo, success, fail){
         const file = blobInfo.blob()
         let param = new FormData()
         param.append('file', file)
         console.log(param.get('file'))
         // 自定义方法，用来获取图片上传后的地址
         getImgUrl(param).then(res => {
             console.log(res)
             const imgUrl = res.data.fileUrl
             success(imgUrl)
         })
     }
     ~~~

#### 4.完整代码（包含子组件和父组件）及最终效果

1. 子组件

   ~~~vue
   <template>
     <div id='tinymce'>
       <section class="tinymce-editor"></section>
     </div>
   </template>
   
   <script>
   import tinymce from 'tinymce/tinymce'
   import 'tinymce/themes/silver/theme'
   import '../../../public/tinymce/zh_CN'
   import 'tinymce/plugins/preview/plugin'
   import 'tinymce/plugins/image/plugin'
   import 'tinymce/plugins/link/plugin'
   import { getImgUrl } from "../../api/mypage";
   
   export default {
     name: 'Tinymce',
     props: {
       value: {
         type: String,
         default: ''
       }
     },
     data () {
       return {
         initObj: {
           selector: '.tinymce-editor',
           language: 'zh_CN',
           /*
           menubar: 'bar1 bar2',
           menu: {
             bar1: { title: '菜单栏1', items: 'copy paste' },
             bar2: { title: '菜单栏2', items: 'cut' }
           }*/
           toolbar1: 'undo redo | styleselect | bold italic | link image | alignleft aligncenter alignright | outdent indent | preview',
           // 工具栏2
           // toolbar2: 'alignleft aligncenter alignright preview',
           plugins: 'preview image link',
           // 监听初始化完成事件
   
           setup: (editor) => {
             editor.on('init', (e) => {
               editor.setContent(this.value)
             })
           },
           // 文件上传事件
           images_upload_handler (blobInfo, success, fail){
             const file = blobInfo.blob()
             let param = new FormData()
             param.append('file', file)
             console.log(param.get('file'))
             getImgUrl(param).then(res => {
               console.log(res)
               const imgUrl = res.data.fileUrl
               success(imgUrl)
             })
           },
           // 监听input 和 change事件 实时更新value
           init_instance_callback: (editor) => {
             editor.on('input', (e) => {
               this.$emit('input', e.target.innerHTML)
             })
             editor.on('change', (e) => {
               this.$emit('input', e.level.content)
             })
           }
         }
       }
     },
     mounted() {
       tinymce.init(this.initObj)
     }
   }
   </script>
   <style lang="less" scoped>
   @import url('~tinymce/skins/ui/oxide/skin.min.css')
   </style>
   ~~~

2. 父组件

   ~~~vue
   <template>
     <div>
       <tinymce v-model="value"></tinymce>
       <div v-html="value"></div>
     </div>
   </template>
   
   <script>
   import Tinymce from '../../components/myTinymce/Tinymce'
   export default {
     data() {
       return {
         value: ''
       }
     },
     components: {
       Tinymce
     }
   }
   </script>
   ~~~

3. 用到的api

   ~~~js
   export function getImgUrl(data) {
     return request({
       url: '/fileapi/file_server/uploadFile',
       method: 'post',
       headers: {
         'Content-Type': 'multipart/form-data'
       },
       data
     })
   }
   ~~~

4. 最终效果

![image-20200313102951015](https://gitee.com/WJH9102/figureBed/raw/master/img/20200513172557.png)