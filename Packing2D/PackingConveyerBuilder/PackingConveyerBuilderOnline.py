__author__ = 'human88998999877'
from Packing2D.PackingConveyer.Filter import Filter
from Packing2D.PackingConveyer.PackingControl.PackingControlOnline import PackingControlOnline
from Packing2D.PackingConveyerBuilder.PackingConveyerBuilder import PackingConveyerBuilder


class PackingConveyerBuilderOnline(PackingConveyerBuilder):
    def _onBuild(self, conveyer, factory, settings):
        filter = Filter(1)
        conveyer.pushUnit( filter )

        packer = factory.createInstance(settings.packingAlgorithm)

        control = PackingControlOnline()
        
        if settings.sortOrder is not None \
            and settings.sortKey is not None:
            #init sorting
            pass

        if settings.binSizeMode is  None:
            pass

        if settings.placeHeuristic is not None:
            pass

        if settings.packingMode is not None:
            pass

        if settings.packingAlgorithmAbility is not None:
            pass
        pass
    pass

  