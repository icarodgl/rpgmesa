<?php

class Item {
   private $nome;
   private $descricao;
   private $peso;
   private $efeito;
   
   
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

   function usar(Personagem $personagem){}
}
