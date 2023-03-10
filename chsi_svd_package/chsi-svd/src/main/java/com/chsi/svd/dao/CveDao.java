package com.chsi.svd.dao;

import com.chsi.svd.pojo.Cve;

import java.util.List;

public interface CveDao {
    /**
     * 根据cve编号获取cve详细信息
     * @param cveName
     * @return
     */
    Cve queryMatchCve(String cveName);
}
