# Java实现office转PDF

# 1.下载libreoffice

[下载地址](https://www.libreoffice.org/download/download/?type=rpm-x86_64&version=7.2.2&lang=zh-CN)，下载完成后安装，Centos下安装后运行可能会报错

> soffice -help
>
> 报错
>
> /opt/libreoffice6.0/program/soffice.bin: error while loading shared libraries: libcairo.so.2: cannot open shared object file: No such file or directory
>
> 执行命令：
>
> yum install cairo
>
> 后再次执行命令：/opt/libreoffice6.0/program/soffice -help
>
> 再次报错
>
> /opt/libreoffice6.0/program/soffice.bin: error while loading shared libraries: libcups.so.2: cannot open shared object file: No such file or directory
>
> 执行命令：
>
> yum install cups-libs
>
> 后，再次执行命令：/opt/libreoffice6.0/program/soffice -help
>
> 报错：
>
> /opt/libreoffice6.0/program/soffice.bin: error while loading shared libraries: libSM.so.6: cannot open shared object file: No such file or directory
>
> 执行命令：
>
> yum install libSM

# 2.Java代码

其本质是使用 libreoffice 的相关命令

```java
package cn.junhaox.toPdf;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

/**
 * @author ibytecode2020@gmail.com
 * create by Wang Junhao
 * @date 2021/11/3 20:39
 */
public class PdfConverter {


    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        String srcPath = "C:\\Users\\wjh\\Desktop\\信科11602王君豪（万立）\\基于Java的新闻平台设计-王君豪\\正文.docx", desPath = "C:/Users/wjh/Desktop/ww";
        String command = "";
        String osName = System.getProperty("os.name");
        if (osName.contains("Windows")) {
            command = "D:/ProgramFiles/LibreOffice/program/soffice.exe --headless --convert-to pdf:writer_pdf_Export  " + srcPath + " --outdir " + desPath;
            exec(command);
        }
        long end = System.currentTimeMillis();
        System.out.println("用时:{} ms" + (end - start));
    }

    public static boolean exec(String command) {
        Process process;// Process可以控制该子进程的执行或获取该子进程的信息
        try {

            process = Runtime.getRuntime().exec(command);// exec()方法指示Java虚拟机创建一个子进程执行指定的可执行程序，并返回与该子进程对应的Process对象实例。
            // 下面两个可以获取输入输出流
            InputStream errorStream = process.getErrorStream();
            InputStream inputStream = process.getInputStream();
            byte[] err = new byte[1024 * 1024];
            byte[] in = new byte[1024 * 1024];
            int errLen = errorStream.read(err);
            int inLen = inputStream.read(in);
            if (errLen > 0) System.out.println("err" + new String(err, 0, errLen, "GBK"));
            if (inLen > 0) System.out.println("in" + new String(in, 0, inLen, "GBK"));

        } catch (IOException e) {
            return false;
        }

        int exitStatus = 0;
        try {
            exitStatus = process.waitFor();// 等待子进程完成再往下执行，返回值是子线程执行完毕的返回值,返回0表示正常结束
            // 第二种接受返回值的方法
            int i = process.exitValue(); // 接收执行完毕的返回值
            System.out.println("i--" + i);
        } catch (InterruptedException e) {
            return false;
        }

        if (exitStatus != 0) {
            System.out.println("exec cmd exitStatus " + exitStatus);
        } else {
            System.out.println("exec cmd exitStatus " + exitStatus);
        }

        process.destroy(); // 销毁子进程
        process = null;

        return true;
    }
}

```
