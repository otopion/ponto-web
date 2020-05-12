<template>
	<nav class="nav flex-column">
	<div class="d-flex" id="wrapper">
	<div class="border-right" id="sidebar-wrapper">
      <div class="sidebar-heading" ><br><br></div>
      <div class="list-group">
        <a v-for="(item, i) in items"
		:key="i">
			<router-link class="nav nav-link" :to="item.url">
			<a class="list-group-item list-group-item-action bg-light">
				<b-icon :icon="item.icon" class="icon" />
				<i id="text">{{ item.text }}</i>
				</a>
			</router-link>
		</a>
      </div>
	</div>
	</div>
		</nav>
</template>

<script>
	export default {
        props: ["items"]
    }
</script>

<style lang="scss">
body {
  overflow-x: hidden;
}
#text{
	color: black;
}

.icon{
	margin-right: 10px;
	color: black;
}

a{
	margin-top: 4px;
}

.d-flex{
	position: fixed;
	background-color: #00aeef;
}

#sidebar-wrapper {
  min-height: 100vh;
  margin-left: -15rem;
  -webkit-transition: margin .25s ease-out;
  -moz-transition: margin .25s ease-out;
  -o-transition: margin .25s ease-out;
  transition: margin .25s ease-out;
}

#sidebar-wrapper .sidebar-heading {
  padding: 0.875rem 1.25rem;
  font-size: 1.2rem;
}

#sidebar-wrapper .list-group {
  width: 15rem;
	background-color: #00aeef;
}

#sidebar-wrapper .list-group-flush {
	background-color: #00aeef;
}

#page-content-wrapper {
  min-width: 100vw;

}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}
#sidebar-wrapper {
	margin-left: 0px;
}
</style>