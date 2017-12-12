INSERT INTO `usuario` (`IdUsuario`, `Username`, `Senha`, `Email`, `DataCadastro`) VALUES (NULL, 'alguem', '123123', 'meu@email.com', '2017-12-11 00:00:00');


INSERT INTO `historia` (`IdHistoria`, `Nome`, `Descricao`, `Capa`) VALUES (NULL, 'Minha Historia', 'em um reino encantado', 'capa.png');

INSERT INTO `personagem` (`IdPersonagem`, `IdUsuario`, `Nome`, `Experiencia`, `Level`, `Saude`, `Imagem`) VALUES (NULL, '1', 'Meu Personagem', '0', '0', '10', 'meupersonagem.jpg');

INSERT INTO `partida` (`IdPartida`, `IdHistoria`, `NomeJogo`) VALUES(NULL, '1', 'Novo Jogo');

INSERT INTO `linhadotempo` (`IdLinhaDoTempo`, `IdPersonagem`, `IdPartida`, `Sucesso`, `Descricao`, `Data`) VALUES (NULL, '1', '3', '1', 'EU ataquei alguem', '2017-12-11 00:00:00');