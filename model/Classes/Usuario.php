<?php
/**
 * Usuario
 * 
 * @Entity
 * @Table(name="Usuario")
 */
class Usuario
{
    /**
     * @Id
     * @Column(type="integer", name="IdUsuario")
     * @GeneratedValue(strategy="AUTO")
     */
    protected $id;
    /**
     * @Column(type="string", name="Username")
     */
    protected $username;
    
    /**
     * @Column(type="string", name="Senha")
     */
    protected $senha;
    
    /**
     * @Column(type="string", name="Email")
     */
    protected $email;
    
    /**
     * @Column(type="datetime", name="DataCadastro")
     */
    protected $dataCadastro;
    
    function __construct() {
        $this->id = 0;
    }

    
    function getId() {
        return $this->id;
    }

    function getUsername() {
        return $this->username;
    }

    function getSenha() {
        return $this->senha;
    }

    function getEmail() {
        return $this->email;
    }

    function getDataCadastro() {
        return $this->dataCadastro;
    }

    function setId($id) {
        $this->id = $id;
    }

    function setUsername($username) {
        $this->username = $username;
    }

    function setSenha($senha) {
        $this->senha = $senha;
    }

    function setEmail($email) {
        $this->email = $email;
    }

    function setDataCadastro($dataCadastro) {
        $this->dataCadastro = $dataCadastro;
    }

    function login($login, $senha){}
    function logout($tolken){}
}