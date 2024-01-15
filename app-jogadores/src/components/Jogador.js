import React, { useState } from 'react';
import axios from 'axios';

function Jogador(props) {
    const [showModal, setShowModal] = useState(false);
    const [selectedJogadorId, setSelectedJogadorId] = useState(null);

    // Função para deletar jogador
    const excluirJogador = (jogadorId) => {
        axios.delete(`http://127.0.0.1:8000/jogadores/${jogadorId}`)
            .then(
                resposta => {
                    alert("Jogador removido com sucesso" + resposta.data)
                    setShowModal(false);
                }
            )
    }

    const confirmarExclusao = (jogadorId) => {
        setSelectedJogadorId(jogadorId);
        setShowModal(true);
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
                    onClick={() => confirmarExclusao(props.jogador.id)}
                    className="btn btn-sm"
                >
                    <span className="badge rounded-pill bg-danger">X</span>
                </button>
            </p>

            {showModal && (
                <div className="modal" style={{ display: 'block' }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Confirmação</h5>
                                <button type="button" className="btn-close" onClick={() => setShowModal(false)}></button>
                            </div>
                            <div className="modal-body">
                                Você tem certeza que deseja excluir o jogador?
                            </div>
                            <div className="modal-footer">
                                <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>
                                    Cancelar
                                </button>
                                <button type="button" className="btn btn-danger" onClick={() => excluirJogador(selectedJogadorId)}>
                                    Sim, excluir
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}

        </div>
    );
}

export default Jogador;
