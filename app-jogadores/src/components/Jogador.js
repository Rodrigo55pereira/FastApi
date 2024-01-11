import React from 'react';
import axios from 'axios';

function Jogador(props) {

    // Função para deletar jogador
    const excluirJogador = (jogadorId) => {
        axios.delete(`http://127.0.0.1:8000/jogadores/${jogadorId}`)
            .then(
                resposta => {
                    alert("Jogador removido com sucesso" + resposta.data)
                }
            )
    }
    const editaJogador = (jogador) => {
        props.setJogadorId(jogador.id)
        props.setJogadorNome(jogador.nome)
        props.setJogadorIdade(jogador.idade)
        props.setJogadorTime(jogador.time)
        props.setTextoBotao("Atualizar")
    }
    return (
        <div>
            <p>
                <span className="fw-bold">
                    {props.jogador.nome} - {props.jogador.idade} - {props.jogador.time}
                </span>
                <button
                    onClick={() => editaJogador(props.jogador)}
                    className="btn btn-sm"
                >
                    <span className="badge rounded-pill bg-info">Editar</span>
                </button>
                <button
                    onClick={() => excluirJogador(props.jogador.id)}
                    className="btn btn-sm"
                >
                    <span className="badge rounded-pill bg-danger">X</span>
                </button>
            </p>
        </div>
    );
}

export default Jogador;
