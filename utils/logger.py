
# ==========================================
# CONFIGURACION DE REGISTRO DE EVENTOS
# Sistema de Gestion Software FJ
# ==========================================

import logging


def configurar_logger():

    logging.basicConfig(
        filename="sistema.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )

    return logging.getLogger("SoftwareFJ")
