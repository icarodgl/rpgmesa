<?php
/**
 * @Entity
 * @InheritanceType("SINGLE_TABLE")
 * @DiscriminatorColumn(name="Class", type="string")
 * @DiscriminatorMap({"Item" = "Item", "Utilizavel" = "Utilizavel", "Armamento" = "Armamento", "Armadura" = "Armadura"})
 */
class Item {
   /**
   * @Id
   * @Column(type="integer", name="IdItem")
   * @GeneratedValue(strategy="AUTO") */
   protected $id;
   /** @Column(type="integer", name="IdFicha") */
   protected $idFicha;
   
   private $class;
   function getClass() {
       return $this->class;
   }

   function setClass($class) {
       $this->class = $class;
   }

      /** @Column(type="string", name="Descricao") */
   private $descricao;
   
   /** @Column(type="integer", name="Peso") */
   private $peso;
   
   /** @Column(type="string", name="Efeito") */
   private $efeito;
   
   /** @Column(type="boolean", name="Equipado") */
   private $equipado;
   
   function getEquipado() {
       return $this->equipado;
   }

   function setEquipado($equipado) {
       $this->equipado = $equipado;
   }

      function getId() {
       return $this->id;
   }

   function getIdFicha() {
       return $this->idFicha;
   }

   function getNome() {
       return $this->nome;
   }

   function getDescricao() {
       return $this->descricao;
   }

   function getPeso() {
       return $this->peso;
   }

   function getEfeito() {
       return $this->efeito;
   }

   function setId($id) {
       $this->id = $id;
   }

   function setIdFicha($idFicha) {
       $this->idFicha = $idFicha;
   }

   function setNome($nome) {
       $this->nome = $nome;
   }

   function setDescricao($descricao) {
       $this->descricao = $descricao;
   }

   function setPeso($peso) {
       $this->peso = $peso;
   }

   function setEfeito($efeito) {
       $this->efeito = $efeito;
   }

      function usar(Personagem $personagem){
       $nome = $personagem->getNome();
       $descricaoRet = "$this->nome foi usado em $nome ";
       return $descricaoRet;
   }

}
