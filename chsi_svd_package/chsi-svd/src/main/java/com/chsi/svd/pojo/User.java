package com.chsi.svd.pojo;

import com.chsi.framework.pojos.PersistentObject;
import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Data
@Table(name = "SVD_USER")
public class User extends PersistentObject {
    @Id
    private String id;
}
