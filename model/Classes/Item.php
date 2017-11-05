<?php
/**
 * @Entity
 */
class Item {
   /**
   * @Id
   * @Column(type="integer", name="IdItem")
   * @GeneratedValue(strategy="AUTO") */
   protected $id;
   /** @Column(type="integer", name="IdFicha") */
   protected $idFicha;
   
   /** @Column(type="string", name="Descricao") */
   private $descricao;
   
   /** @Column(type="integer", name="Peso") */
   private $peso;
   
   /** @Column(type="string", name="Efeito") */
   private $efeito;
   
   /** @Column(type="boolean", name="Equipado") */
   private $equipado;
   
   /** @Column(type="integer", name="Tempo") */
   private $tempo;
   
   /** @Column(type="integer", name="Dano") */
   private $dano;
   
   /** @Column(type="integer", name="Cargas") */
   private $cargas;
   
   /** @Column(type="integer", name="Acerto") */
   private $acerto;
   
   /** @Column(type="integer", name="Mao") */
   private $mao;
   
   /** @Column(type="integer", name="TipoDado") */
   private $tipoDado;
   
   /** @Column(type="integer", name="QuatDado") */
   private $quatDado;
   
   /** @Column(type="integer", name="Defesa") */
   private $defesa;
   
   /** @Column(type="integer", name="Agilidade") */
   private $agilidade;
   
   /** @Column(type="integer", name="Arcano") */
   private $arcano;
   
   function getId() {
       return $this->id;
   }

   function getIdFicha() {
       return $this->idFicha;
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

   function getEquipado() {
       return $this->equipado;
   }

   function getTempo() {
       return $this->tempo;
   }

   function getDano() {
       return $this->dano;
   }

   function getCargas() {
       return $this->cargas;
   }

   function getAcerto() {
       return $this->acerto;
   }

   function getMao() {
       return $this->mao;
   }

   function getTipoDado() {
       return $this->tipoDado;
   }

   function getQuatDado() {
       return $this->quatDado;
   }

   function getDefesa() {
       return $this->defesa;
   }

   function getAgilidade() {
       return $this->agilidade;
   }

   function getArcano() {
       return $this->arcano;
   }

   function setId($id) {
       $this->id = $id;
   }

   function setIdFicha($idFicha) {
       $this->idFicha = $idFicha;
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

   function setEquipado($equipado) {
       $this->equipado = $equipado;
   }

   function setTempo($tempo) {
       $this->tempo = $tempo;
   }

   function setDano($dano) {
       $this->dano = $dano;
   }

   function setCargas($cargas) {
       $this->cargas = $cargas;
   }

   function setAcerto($acerto) {
       $this->acerto = $acerto;
   }

   function setMao($mao) {
       $this->mao = $mao;
   }

   function setTipoDado($tipoDado) {
       $this->tipoDado = $tipoDado;
   }

   function setQuatDado($quatDado) {
       $this->quatDado = $quatDado;
   }

   function setDefesa($defesa) {
       $this->defesa = $defesa;
   }

   function setAgilidade($agilidade) {
       $this->agilidade = $agilidade;
   }

   function setArcano($arcano) {
       $this->arcano = $arcano;
   }


}
