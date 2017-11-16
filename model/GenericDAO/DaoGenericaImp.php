<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of DaoGenericaImp
 *
 * @author icaro
 */
use Doctrine\Common\Cache\ArrayCache;
use Doctrine\ORM\Configuration;
use Doctrine\ORM\EntityManager;
use Doctrine;
use Doctrine\DBAL\Connection;
use Doctrine\DBAL\DriverManager;

class DaoGenericaImp implements DaoGenerica {

    private $entityManager;
    private $connectionParameters;
    private $connectionConfig;
    private $searchesWithLocaleOrder;

    public function __construct(array $options) {
        $this->entityManager = $this->getEntityManager($options);
    }

    public function alterar($objeto) {
        $em = $this->getEntityManager();
        $em->persist($objeto);
        $em->flush($objeto);
        return $objeto;
    }

    public function deletar($objeto) {
        $em = $this->getEntityManager();
        $em->remove($objeto);
        $em->flush($objeto);
    }

    public function inserir($objeto) {
        $em = $this->getEntityManager();
        $em->persist($objeto);
        $em->flush($objeto);
        return $objeto;
    }

    public function listar($objeto) {
        $em = $this->getEntityManager();
        return $em->getRepository($objeto)->findAll();
    }

    /**
     * 
     * @param string $entityQuery
     * @param array $parameters
     * @return type
     * 
     * 
     */
    public function getResult(string $entityQuery, array $parameters = null) {
        $em = $this->getEntityManager();
        $query = $em->createQuery($entityQuery);
        if (!is_null($parameters)) {
            $query->setParameters($parameters);
        }
        return $query->getResult();
    }

    public function getResultSet(string $sql, array $parameters = null) {
        try {
            $connection = $this->getConnection();
            $connection->connect();

            $statement = $connection->prepare($sql);
            if (!is_null($parameters)) {
                $i = 1;
                foreach ($parameters as $parameter) {
                    $statement->bindValue($i++, $parameter);
                }
            }

            $statement->execute();

            return $statement->fetchAll();
        } finally {
            $connection->close();
        }
    }

    public function beginTransaction() {
        $em = $this->getEntityManager();
        $em->getConnection()->beginTransaction();
    }

    public function commit() {
        $em = $this->getEntityManager();
        $em->getConnection()->commit();
        $em->getConnection()->close();
    }

    public function rollBack() {
        $em = $this->getEntityManager();
        $em->getConnection()->rollBack();
        $em->getConnection()->close();
    }

    public function refresh($entity) {
        $em = $this->getEntityManager();
        $em->refresh($entity);
    }

    public function getEntityManager(array $options = null) {
        if (is_null($this->entityManager) && !is_null($options)) {
            // TODO must be implement validations of requiment sets and throws exception
            $config = new Configuration();
            $cache = new ArrayCache();
            // configuring the path of model classes
            $driverImpl = $config->newDefaultAnnotationDriver($options['modelDir']);
            // configuring cache
            $config->setMetadataCacheImpl($cache);
            $config->setQueryCacheImpl($cache);
            //configuring data proxies, por auto generation de proxies (lazy-load)
            $config->setProxyDir($options['proxyDir']);
            $config->setProxyNamespace($options['proxyNamespace']);
            $config->setAutoGenerateProxyClasses($options['autoGenerateProxyClasses']);
            $config->setMetadataDriverImpl($driverImpl);
            $this->connectionConfig = $config;
            $this->searchesWithLocaleOrder = $options['searchesWithLocaleOrder'];
            /**
             * @var array $dataConnection
             * creating other array for database configuration
             * just for use a unique parameter on method (for dont have two arrays)
             */
            $dataConnection = $this->arrayConection($options);
            
            //keep parameters for connection
            $this->connectionParameters = $dataConnection;
            $this->entityManager = EntityManager::create($dataConnection, $config);
        }
        return $this->entityManager;
    }
    function arrayConection($options){
        $dataConnection = array();
        $dataConnection["driver"] = $options["driver"];
        $dataConnection["host"] = $options["localhost"];
        $dataConnection["dbname"] = $options["rpgmesa"];
        $dataConnection["user"] = $options["user"];
        $dataConnection["password"] = $options["123123"];
        $dataConnection["charset"] = $options["charset"];
        return $dataConnection;
    }

    private function getConnection(): Connection {
        return DriverManager::getConnection($this->connectionParameters, $this->connectionConfig);
    }

}
