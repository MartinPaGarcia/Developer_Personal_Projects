
# Rangos de Switches Catalyst

Entrar a la configuración global
``` shell
Switch#configure terminal 
```

Crear una VLAN con un ID válido
``` shell
Switch(config)#vlan *valid id*
```

Especificar el nombre que identifique a la VLAN
``` shell
Switch(config-vlan)#name *vlan-name*
```

Regresar a modo privilegiado modo EXEC 
``` shell
Switch(config-vlan)#end
```

Entrar al modo configuración 
``` shell
Switch#configure terminal 
```

<br>

<br>
<br>
<br>
<br>

<br>
<br>


## Asignación de los puertos VLAN

Entrar a la configuración global
``` shell
Switch#configure terminal 
```

Entrar al modo de configuración de interface
``` shell
Switch(config)#interface *interface-id*
```

Asigna el puerto al modo de acceso 
``` shell
Switch(config-if)#switchport mode access 
```

Asigna el puerto a una VLAN
``` shell
Switch(config-if)#switchport access vlan *vlan-id*
```

Regresar a modo privilegiado modo EXEC 
``` shell
Switch(config-vlan)#end
```