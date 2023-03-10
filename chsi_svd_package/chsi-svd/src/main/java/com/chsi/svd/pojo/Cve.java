package com.chsi.svd.pojo;

import com.chsi.framework.pojos.PersistentObject;
import lombok.Data;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

@Data
@Entity
@Table(name = "SVD_CVE_LIST1")
public class Cve extends PersistentObject{
    @Id
    @GeneratedValue(generator = "pk_id")
    @GenericGenerator(name = "pk_id", strategy = "com.chsi.framework.hibernate.StringRandomGenerator")
    @Column(name = "ID", length = 32)
    private String id;


    @Column(name = "CVE_NAME")
    private String cveName;
    @Column(name = "CVE_URL")
    private String url;
    @Column(name = "CVE_CNA_SCORE")
    private String cnaScore;
    @Column(name = "CVE_NIST_SCORE")
    private String nistScore;
    @Column(name = "CVE_DESC")
    private String desc;
    @Column(name = "CVE_PUBLIC")
    private String publicTime;
    @Column(name = "CVE_LAST_MODIFIED")
    private String lastModified;
    @Column(name = "CVE_TYPE_ID")
    private String cweId;
    @Column(name = "CVE_REFERER")
    private String referers;
}
