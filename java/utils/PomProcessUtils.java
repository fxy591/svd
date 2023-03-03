package utils;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class PomProcessUtils {
    public static String str = "chsi";

    /**
     * 从pom文件获取文件全部内容
     * @param filename 文件路径
     * @return string
     * @throws IOException
     */
    public static String getFile(String path) throws IOException {
        File file = new File(path);
        Long fileLength = file.length(); // 获取文件长度
        byte[] fileContent = new byte[fileLength.intValue()];
        FileInputStream in = new FileInputStream(file);
        in.read(fileContent);
        in.close();
        return new String(fileContent);
    }

    /**
     * 从pom文件中获取全部groupid
     * @param pom
     * @return groupid list
     * @throws IOException
     */
    public static List<String> getGroup(String pom) throws IOException{
        String reg = "(?<dependency><groupId>).*(?=</groupId>)";
        Pattern p = Pattern.compile(reg);
        Matcher m = p.matcher(pom);
//        m.find();
        List<String> strings = new ArrayList<>();
        while (m.find()){
            if(!m.group().contains(str)){
                strings.add(m.group().substring(9));
            }
        }
        return strings;
    }

    public static List<String> getArtifact(String pom) throws IOException{
        String reg = "(?<groupId><artifactId>).*(?=</artifactId>)";
        Pattern p = Pattern.compile(reg);
        Matcher m = p.matcher(pom);
        List<String> strings = new ArrayList<>();
//        m.find();
//        m.find();
        while (m.find()){
            if(!m.group().contains(str)){
                strings.add(m.group().substring(12));
            }
        }
        return strings;
    }

    public static List<String> getVersion(String pom) throws IOException{
        String reg = "(?<artifactId><version>).*(?=</version>)";
        Pattern p = Pattern.compile(reg);
        Matcher m = p.matcher(pom);
        List<String> strings = new ArrayList<>();
        m.find();
        while (m.find()){
            if(!m.group().contains(str)){
                strings.add(m.group().substring(9));
            }
        }
        return strings;
    }
}
