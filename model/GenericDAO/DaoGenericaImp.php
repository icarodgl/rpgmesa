<?php


use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

class DaoGenericaImp implements DaoGenerica {
    
    private $entidades = array("model/Classes");
    private $isDevMode = true;
    private $dbParams = array(
    'driver'   => 'pdo_mysql',
    'user'     => 'root',
    'password' => 'root',
    'dbname'   => 'rpgmesaDB');
    
    private $entityManager = null;
    
    public function __construct() {
        $this->getEntityManager();
    }

    public function alterar($objeto) {
        $this->getEntityManager();
        $this->entityManager->persist($objeto);
        $this->entityManager->flush($objeto);
        return $objeto;
    }

    public function deletar($objeto) {
        $this->getEntityManager();
        $this->entityManager->remove($objeto);
        $this->entityManager->flush($objeto);
    }

    public function inserir($objeto) {
        $this->getEntityManager();
        $this->entityManager->persist($objeto);
        $this->entityManager->flush($objeto);
        return $objeto;
    }

    public function listar($objeto) {
        $this->getEntityManager();
        return $this->entityManager->getRepository($objeto)->findAll();
    }

    public function getResult(string $entityQuery, array $parameters = null) {
        $this->getEntityManager();
        $query = $this->entityManager->createQuery($entityQuery);
        if (!is_null($parameters)) {
            $query->setParameters($parameters);
        }
        return $query->getResult();
    }

    public function getResultSet(string $sql, array $parameters = null) {
        $this->getEntityManager();
        try {
            $connection = $this->entityManager->getConnection();
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
        $this->getEntityManager();
        $this->entityManager->getConnection()->beginTransaction();
    }

    public function commit() {
        $this->getEntityManager();
        $this->entityManager->getConnection()->commit();
        $this->entityManager->getConnection()->close();
    }

    public function rollBack() {
        $this->getEntityManager();
        $this->$entityManager->getConnection()->rollBack();
        $this->$entityManager->getConnection()->close();
    }

    public function refresh($entity) {
       $this->getEntityManager();
        $this->entityManager->refresh($entity);
    }

    public function getEntityManager() {
        
        if ($this->entityManager == null){
            $config = Setup::createAnnotationMetadataConfiguration($this->entidades, $this->isDevMode);
            $this->entityManager = EntityManager::create($this->dbParams, $config);
        }
        return $this->entityManager;
    }
}
