package com.chsi.svd.dao;

import com.chsi.svd.pojo.Component;

public interface ComponentDao {
    /**
     * 根据坐标获取cve编号
     * @param component
     */
    void finCVEData(Component component);
}
