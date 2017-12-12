<?php
namespace model\GenericDAO;
use model\GenericDAO\DaoGenerica;
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;
use Doctrine\DBAL\Logging\EchoSQLLogger;
use Symfony\Component\Console\Input\StringInput;
require_once 'DaoGenerica.php';
require_once "../vendor/autoload.php";

class DaoGenericaImp implements DaoGenerica {
    private $conn;
    private $entidades = array(__DIR__ . "/model/Classes", __DIR__ . "/model/Classes/Personagem");
    private $isDevMode = true;
    private $dbParams = array(
    'driver'   => 'pdo_mysql',
    'user'     => 'root',
    'password' => 'root',
    'dbname'   => 'rpgmesaDB');
    
    private $entityManager = NULL;
    
    public function __construct() {
        $this->getEntityManager();
        $this->conexao();
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
        return $this->entityManager->getRepository(get_class($objeto))->findAll();
    }

    public function getResult(string $sql) {
    
        $this->conexao();
        $result = $this->conn->query($sql);
        $this->conn->close();
        return $result;
 
    }

    public function setQuery(string $sql) {
        $this->conexao();
        if ($this->conn->query($sql)) {
            $this->conn->close();
            return true;
        } else {
            $this->conn->close();
            return true;
        }
        }

/*
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
    */
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
        $this->entityManager->getConnection()->rollBack();
        $this->entityManager->getConnection()->close();
    }

    public function refresh($entity) {
       $this->getEntityManager();
        $this->entityManager->refresh($entity);
    }

    public function getEntityManager() {
        
        if ($this->entityManager === NULL){
            $config = Setup::createAnnotationMetadataConfiguration($this->entidades, $this->isDevMode);
            $this->entityManager = EntityManager::create($this->dbParams, $config);
        }
        return $this->entityManager;
    }


    public function conexao(){
        $servername = "localhost";
        $username = "root";
        $password = "root";
        $dbname = "rpgmesaDB";
        $this->conn = new \mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($this->conn->connect_error) {
            die("Connection failed: " . $this->conn->connect_error);
        }        


    }
}
