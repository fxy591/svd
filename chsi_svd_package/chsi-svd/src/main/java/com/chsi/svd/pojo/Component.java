package com.chsi.svd.pojo;

import javax.persistence.*;

import com.chsi.framework.pojos.PersistentObject;
import lombok.Data;
import org.hibernate.annotations.GenericGenerator;

import java.util.ArrayList;
import java.util.List;

@Entity
@Data
@Table(name = "SVD_COMPONENT_INFO")
public class Component extends PersistentObject{

    @Id
    @GeneratedValue(generator = "pk_id")
    @GenericGenerator(name = "pk_id", strategy = "com.chsi.framework.hibernate.StringRandomGenerator")
    @Column(name = "ID", length = 32)
    private String id;

    @Column(name = "GROUP_ID")
    private String groupId;
    @Column(name = "ARTIFACT_ID")
    private String artifactId;
    @Column(name = "VERSION")
    private String version;
    @Column(name = "CVE_ID")
    private String cve;

    @Transient
    private List<Cve> cveList = new ArrayList<Cve>();

}
