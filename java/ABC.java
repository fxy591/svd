import utils.PomProcessUtils;

import java.io.IOException;
import java.util.List;

public class ABC {
    public static void main(String[] args) throws IOException {
        String path = "D:\\IDEAProjects\\chsi_corp_package\\chsi-corp\\pom.xml";
        String pom = PomProcessUtils.getFile(path);
        List<String> group = PomProcessUtils.getGroup(pom);
        List<String> artifact = PomProcessUtils.getArtifact(pom);
        List<String> version = PomProcessUtils.getVersion(pom);

        for (int i = 0; i < group.size(); i++) {
            System.out.println("group:"+group.get(i)+" artifact:"+artifact.get(i)+" version:"+version.get(i));
        }

    }

    public void jarDetect(){
        String groupId = "";
        String artifactId = "";
        String version = "";

        String sql = "select cve_id from svd_component_info where group_id=:1 and artifact_id=:2 and version=:3";

        String cve_id = "";
        if(cve_id != null){
            // todo： 返回信息
        }
        else {
            // todo: 组件安全
        }
    }
}
